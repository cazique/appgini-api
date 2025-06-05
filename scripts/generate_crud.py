import os
import sys
import inspect as py_inspect # Renaming standard library inspect to avoid conflict
import re
from pathlib import Path
from sqlalchemy import inspect as sqlalchemy_inspect # Importing sqlalchemy.inspect
from typing import List, Dict, Any, Optional, Union, Type, get_origin, get_args

# Add repository root to sys.path to allow imports from 'app'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# SQLAlchemy and Pydantic related imports will be grouped with their respective sections
# For now, ensure we can import Base from database
try:
    from app.models.database import Base
    # We'll need to import all models to ensure they are registered with Base.metadata
    import app.models
except ImportError as e:
    print(f"Error: Could not import Base or app.models. Ensure they are correctly set up. Details: {e}")
    print("Please make sure that app/models/__init__.py imports all your model classes.")
    print(f"Current sys.path: {sys.path}")
    sys.exit(1)

# Output directory constants
SCHEMAS_OUTPUT_DIR = Path("app/schemas")
CRUD_OUTPUT_DIR = Path("app/crud")
ENDPOINTS_OUTPUT_DIR = Path("app/api/api_v1/endpoints")
API_ROUTER_FILE = Path("app/api/api_v1/api.py")
MAIN_APP_FILE = Path("app/main.py")


# Utility functions for naming conventions
def to_snake_case(name: str) -> str:
    """Converts CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_plural(name: str) -> str:
    """Converts a singular noun to plural (simple version)."""
    if name.endswith('y') and not name.endswith('ay') and not name.endswith('ey') and not name.endswith('iy') and not name.endswith('oy') and not name.endswith('uy'):
        return name[:-1] + 'ies'
    elif name.endswith('s') or name.endswith('sh') or name.endswith('ch') or name.endswith('x') or name.endswith('z'):
        return name + 'es'
    else:
        return name + 's'

def get_sqlalchemy_models() -> List[Type[Base]]:
    """Discovers all SQLAlchemy models registered with Base.metadata."""
    models = []
    # Ensure all models are imported by accessing app.models attributes
    # This relies on app/models/__init__.py having an __all__ or importing them directly
    if hasattr(app.models, '__all__'):
        for model_name in app.models.__all__:
            if model_name not in ["Base", "engine", "SessionLocal", "get_db"]: # Exclude non-model exports
                model_class = getattr(app.models, model_name, None)
                if model_class and isinstance(model_class, type) and issubclass(model_class, Base) and model_class is not Base:
                    models.append(model_class)
    else: # Fallback if no __all__
        for name, obj in inspect.getmembers(app.models):
            if inspect.isclass(obj) and issubclass(obj, Base) and obj is not Base:
                 # Check if it's defined in app.models.* submodules, not imported from elsewhere
                if obj.__module__.startswith('app.models.'):
                    models.append(obj)

    if not models:
        print("Warning: No SQLAlchemy models found. Make sure they are imported in app/models/__init__.py and inherit from Base.")
    return list(set(models)) # Use set to ensure uniqueness if imported multiple ways

# --- Pydantic Schema Generation ---

# Mapping SQLAlchemy types to Pydantic types and Python standard types
# SQLALCHEMY_TO_PYDANTIC_TYPE_MAP is not used with isinstance approach below, can be removed or kept for reference
PYTHON_TO_PYDANTIC_IMPORTS = {
    "Decimal": "from decimal import Decimal",
    "date": "from datetime import date",
    "datetime": "from datetime import datetime",
    "time": "from datetime import time",
    "List": "from typing import List",
    "Optional": "from typing import Optional",
    "Any": "from typing import Any",
}

def get_pydantic_field_type(column, model_name_map, is_optional_overall=False) -> tuple[str, List[str]]:
    """Determines the Pydantic field type string and necessary imports for a SQLAlchemy column."""
    imports = []
    python_type = None

    from sqlalchemy import String, Text, Integer, SmallInteger, BigInteger, Float, Numeric, Boolean, Date, DateTime, Time

    if isinstance(column.type, DateTime):
        python_type = "datetime"
        if "datetime" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["datetime"])
    elif isinstance(column.type, Date):
        python_type = "date"
        if "date" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["date"])
    elif isinstance(column.type, Time):
        python_type = "time"
        if "time" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["time"])
    elif isinstance(column.type, String) or isinstance(column.type, Text):
        python_type = "str"
    elif isinstance(column.type, Integer) or isinstance(column.type, SmallInteger) or isinstance(column.type, BigInteger):
        python_type = "int"
    elif isinstance(column.type, Float):
        python_type = "float"
    elif isinstance(column.type, Numeric):
        python_type = "Decimal"
        if "Decimal" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["Decimal"])
    elif isinstance(column.type, Boolean):
        python_type = "bool"
    else:
        col_type_str = str(column.type)
        python_type = "Any"
        if "Any" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["Any"])
        print(f"Warning: Could not map SQLAlchemy type '{col_type_str}' to Pydantic type for column '{column.name}'. Defaulting to 'Any'.")

    is_optional = column.nullable or is_optional_overall
    if hasattr(column, 'server_default') and column.server_default is not None:
        is_optional = True
    if hasattr(column, 'default') and column.default is not None:
        is_optional = True

    if is_optional:
        final_type = f"Optional[{python_type}]"
        if "Optional" in PYTHON_TO_PYDANTIC_IMPORTS: imports.append(PYTHON_TO_PYDANTIC_IMPORTS["Optional"])
        # Ensure the inner type's import is also included if it was Any
        if python_type == "Any" and "Any" in PYTHON_TO_PYDANTIC_IMPORTS and PYTHON_TO_PYDANTIC_IMPORTS["Any"] not in imports:
            imports.append(PYTHON_TO_PYDANTIC_IMPORTS["Any"])
        return final_type + " = None", list(set(imports))
    else:
        return python_type, list(set(imports))

def generate_pydantic_schemas(model_class: Type[Base], all_models: List[Type[Base]]):
    model_name = model_class.__name__
    model_name_snake = to_snake_case(model_name)
    print(f"Generating Pydantic schemas for {model_name}...")

    model_name_map = {m.__name__: m for m in all_models}
    fields_base_dict = {} # Use dict to avoid duplicate PKs if base includes them by default
    fields_create_list = []
    fields_read_relations_list = []

    all_imports = set(["from pydantic import BaseModel"]) # Removed Optional, List, Any for more targeted import
                                                        # Will be added by get_pydantic_field_type or relationship logic

    inspector = sqlalchemy_inspect(model_class)
    pk_names = {pk_col.name for pk_col in inspector.primary_key}

    # Define Base schema fields
    for column in inspector.columns:
        col_name = column.name
        field_type_str_base, field_imports_base = get_pydantic_field_type(column, model_name_map)
        fields_base_dict[col_name] = f"    {col_name}: {field_type_str_base}"
        all_imports.update(field_imports_base)

    # Define Create schema fields (inherits from Base, excludes auto-gen PKs, respects required fields)
    for column in inspector.columns:
        col_name = column.name
        if column.primary_key and column.autoincrement:
            continue # Exclude auto-incrementing PKs from create schema

        is_required_for_create = not column.nullable and column.default is None and column.server_default is None
        field_type_str_create, field_imports_create = get_pydantic_field_type(column, model_name_map, is_optional_overall=not is_required_for_create)
        # If it's in Base and required for create, it doesn't need to be redefined unless type changes (not changing here)
        # If it's optional in Base but required in Create, it needs redefinition.
        # Current get_pydantic_field_type makes it non-Optional if is_required_for_create is True.
        # So, we only add if the resulting type string is different from base or not in base (e.g. non-column field)
        # For simplicity now, create will list all its fields explicitly.
        fields_create_list.append(f"    {col_name}: {field_type_str_create}")
        all_imports.update(field_imports_create)

    # Define Read schema relationship fields
    forward_refs_needed = set()
    for name, rel_prop in inspector.relationships.items():
        related_model_name = rel_prop.mapper.class_.__name__
        forward_refs_needed.add(related_model_name)
        related_schema_name = f"'{related_model_name}'"

        if rel_prop.uselist:
            field_type = f"Optional[List[{related_schema_name}]] = None" # Default to None for lists too
            if "List" in PYTHON_TO_PYDANTIC_IMPORTS: all_imports.add(PYTHON_TO_PYDANTIC_IMPORTS["List"])
            if "Optional" in PYTHON_TO_PYDANTIC_IMPORTS: all_imports.add(PYTHON_TO_PYDANTIC_IMPORTS["Optional"])
        else:
            field_type = f"Optional[{related_schema_name}] = None"
            if "Optional" in PYTHON_TO_PYDANTIC_IMPORTS: all_imports.add(PYTHON_TO_PYDANTIC_IMPORTS["Optional"])
        fields_read_relations_list.append(f"    {name}: {field_type}")

    # --- Assemble file content ---
    # Imports first
    file_content_parts = [ "\n".join(sorted(list(all_imports))) + "\n\n"]

    # Schema Base
    schema_base_name = f"{model_name}Base"
    file_content_parts.append(f"class {schema_base_name}(BaseModel):")
    if fields_base_dict:
        file_content_parts.extend(fields_base_dict.values())
    else:
        file_content_parts.append("    pass")
    file_content_parts.append("\n")

    # Schema Create
    schema_create_name = f"{model_name}Create"
    file_content_parts.append(f"class {schema_create_name}({schema_base_name}):")
    if fields_create_list: # Create schema lists its own fields, could inherit and override too
        # Alternative: inherit and only list fields that differ or are added
        # For now, explicitly listing all create fields if any, else pass
        temp_create_fields = []
        base_field_names_for_create = {k:v for k,v in fields_base_dict.items() if not (k in pk_names and any(insp_col.autoincrement for insp_col in inspector.primary_key if insp_col.name == k))}

        for col_name, base_field_def_str in base_field_names_for_create.items():
            column_obj = inspector.columns[col_name]
            is_required_for_create = not column_obj.nullable and column_obj.default is None and column_obj.server_default is None

            # If required for create and it was optional in base, use non-optional type
            if is_required_for_create and "Optional[" in base_field_def_str:
                 field_type_str_required, _ = get_pydantic_field_type(column_obj, model_name_map, is_optional_overall=False)
                 temp_create_fields.append(f"    {col_name}: {field_type_str_required}")
            else: # Otherwise, use the definition from base (which includes Optional if applicable)
                 temp_create_fields.append(base_field_def_str)

        file_content_parts.extend(temp_create_fields if temp_create_fields else ["    pass"])

    else: # No specific create fields (e.g. all are auto-PKs or inherited as is)
        file_content_parts.append("    pass")
    file_content_parts.append("\n")

    # Schema Update
    schema_update_name = f"{model_name}Update"
    file_content_parts.append(f"class {schema_update_name}(BaseModel):")
    update_fields = []
    for column in inspector.columns:
        if column.name in pk_names:
            continue
        field_type_str, field_imports = get_pydantic_field_type(column, model_name_map, is_optional_overall=True)
        update_fields.append(f"    {column.name}: {field_type_str}")
        all_imports.update(field_imports) # Ensure imports for update fields are captured (though mostly Optional)

    if update_fields:
        file_content_parts.extend(update_fields)
    else:
        file_content_parts.append("    pass")
    file_content_parts.append("\n")

    # Schema Read (Main)
    schema_read_name = f"{model_name}"
    file_content_parts.append(f"class {schema_read_name}({schema_base_name}):")
    # Read schema inherits all fields from Base, and adds relationship fields.
    # PKs are already in Base.
    if fields_read_relations_list:
        file_content_parts.extend(fields_read_relations_list)
    else: # No relationships, but still need a body if Base was empty
        if not fields_base_dict : file_content_parts.append("    pass")
        elif not fields_read_relations_list: # If base has fields but no new relations
             pass # No need to add 'pass' if base fields exist

    file_content_parts.append("    class Config:")
    file_content_parts.append("        from_attributes = True  # Pydantic V2 setting")
    file_content_parts.append("\n")

    # Forward reference resolution for Pydantic v1 (string types usually enough for v2)
    # This is typically done at the end of the file, after all classes are defined.
    # For Pydantic v2, explicit update_forward_refs() is less common if using string annotations.
    # However, if models are in different files and import each other for type hints in relationships,
    # string annotations ('ClassName') are key. The schema loader or main app usually handles resolution.
    # For now, relying on string annotations and correct imports in __init__.py of schemas.

    # Separate imports for standard types and related model schemas
    standard_imports = list(all_imports)
    related_schema_imports = []

    if forward_refs_needed:
        standard_imports.append("from typing import TYPE_CHECKING") # Add TYPE_CHECKING import itself
        for ref_model_name in forward_refs_needed:
            if ref_model_name != model_name:
                related_model_schema_import_name = ref_model_name
                import_line = f"    from .{to_snake_case(ref_model_name)} import {related_model_schema_import_name}"
                if import_line not in related_schema_imports:
                    related_schema_imports.append(import_line)

    # Assemble the file content
    file_content_parts_final = [ "\n".join(sorted(standard_imports)) + "\n\n"]

    if related_schema_imports:
        file_content_parts_final.append("if TYPE_CHECKING:")
        file_content_parts_final.extend(sorted(related_schema_imports))
        file_content_parts_final.append("\n")

    file_content_parts_final.extend(file_content_parts) # Add the actual schema class definitions

    file_content = "\n".join(file_content_parts_final)

    schema_file_path = SCHEMAS_OUTPUT_DIR / f"{model_name_snake}.py"
    with open(schema_file_path, "w") as f:
        f.write(file_content)
    print(f"  Generated schema file: {schema_file_path}")

# --- CRUD Function Generation ---
def generate_crud_functions(model_class: Type[Base], schema_create_name: str, schema_update_name: str):
    model_name = model_class.__name__
    model_name_snake = to_snake_case(model_name)
    model_name_lower = model_name_snake

    # Try to get the type of the primary key
    pk_name_for_template: str
    pk_type_hint: str
    pk_column_obj_for_type: Optional[Any] = None

    try:
        # Get the first column of the primary key
        pk_column_obj_for_type = sqlalchemy_inspect(model_class).primary_key[0]
        pk_name_for_template = pk_column_obj_for_type.name

        # Determine PK type for type hinting in the function signature
        _pk_type_str, _ = get_pydantic_field_type(pk_column_obj_for_type, {}, is_optional_overall=False)
        pk_type_hint = _pk_type_str.split(":")[0].strip().split("=")[0].strip() # Get "int" or "str"
        if pk_type_hint == "Any":
            pk_type_hint = "int" # Default assumption for Any if type detection was Any
    except (IndexError, TypeError): # No PK found or other issue with inspect
        print(f"Warning: Could not determine PK for {model_name} via SQLAlchemy inspect. Defaulting to 'id' (name) and 'Any' (type hint).")
        pk_name_for_template = "id" # Default PK name if none found by inspect
        pk_type_hint = "Any"


    print(f"Generating CRUD functions for {model_name}...")

    # Ensure model_name itself is the string name of the class for the template
    model_name_str = model_name # model_name is already class.__name__ which is a string

    # This is the literal string for "ModelName.pk_column_name" to be used in generated code
    model_dot_pk_template = f"{model_name_str}.{pk_name_for_template}"

    crud_content = f"""\
from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.models.{model_name_snake} import {model_name_str} # Use model_name_str for consistency
from app.schemas.{model_name_snake} import {schema_create_name}, {schema_update_name}

# Note: get_multi might need more sophisticated filtering/ordering in a real app

def get(db: Session, id: {pk_type_hint}) -> Optional[{model_name_str}]:
    return db.query({model_name_str}).filter({model_dot_pk_template} == id).first()

def get_multi(db: Session, *, skip: int = 0, limit: int = 100) -> List[{model_name_str}]:
    return db.query({model_name_str}).offset(skip).limit(limit).all()

def create(db: Session, *, obj_in: {schema_create_name}) -> {model_name_str}:
    db_obj = {model_name_str}(**obj_in.model_dump())  # Pydantic v2
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(
    db: Session,
    *,
    db_obj: {model_name_str},
    obj_in: Union[{schema_update_name}, Dict[str, Any]]
) -> {model_name_str}:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True) # Pydantic v2

    # Ensure db_obj is not None before proceeding
    if db_obj is None:
        return None # Or raise HTTPException(status_code=404, detail="Object not found")

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, *, id: {pk_type_hint}) -> Optional[{model_name}]:
    # For getattr, pk_name needs to be a string.
    # getattr(model_name, pk_column.name if pk_column else 'id') would try to get attribute from the class name string.
    # It should be getattr(globals()[model_name], pk_column.name if pk_column else 'id') or pass model_class
    # The current context is an f-string being written to a file, so {model_name} is correct there.
    # The filter line inside the generated file should be:
    # obj = db.query(ModelName).filter(getattr(ModelName, "pk_attr_name") == id).first()
    # However, .get(id) is simpler if the PK type hint matches the actual PK type and it's a single PK.
    # The DDL parsing for PKs currently assumes 'id' or the first found PK.
    # If pk_name_for_template defaults to "id", this will use ModelName.id
    obj = db.query({model_name_str}).filter({model_dot_pk_template} == id).first()
    # A more robust get for single PKs would be:
    # obj = db.get({model_name_str}, id) # if pk_type_hint is guaranteed to match actual PK type
    # However, the filter approach is more general.
    if obj:
        db.delete(obj)
        db.commit()
    return obj
"""
    crud_file_path = CRUD_OUTPUT_DIR / f"crud_{model_name_snake}.py"
    with open(crud_file_path, "w") as f:
        f.write(crud_content)
    print(f"  Generated CRUD file: {crud_file_path}")


# --- FastAPI Router Generation ---
def generate_fastapi_router(model_class: Type[Base], crud_module_name_import: str, schema_read_name: str, schema_create_name: str, schema_update_name: str):
    model_name = model_class.__name__
    model_name_snake = to_snake_case(model_name)
    # model_name_plural_snake = to_plural(model_name_snake) # Path usually plural

    # Determine PK type for path parameter and CRUD function calls
    pk_name_for_path = "id" # Default path parameter name
    pk_type_hint = "Any"    # Default type hint for path parameter
    pk_attr_name = "id"     # Default attribute name on the model

    try:
        pk_column = sqlalchemy_inspect(model_class).primary_key[0]
        pk_attr_name = pk_column.name
        # Get Pydantic type for path parameter type hint
        _pk_type_str, _ = get_pydantic_field_type(pk_column, {}, is_optional_overall=False)
        pk_type_hint = _pk_type_str.split(":")[0].strip().split("=")[0].strip()
        if pk_type_hint == "Any": pk_type_hint = "int" # Default if Any
    except IndexError: # No PK found
        print(f"Warning: No PK found for {model_name} for router generation. Defaulting to 'id: Any'.")


    print(f"Generating FastAPI router for {model_name}...")

    router_content = f"""\
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.{schema_read_name})
def create_{model_name_snake}(
    *,
    db: Session = Depends(deps.get_db),
    {model_name_snake}_in: schemas.{schema_create_name}
) -> models.{model_name}:
    \"\"\"
    Create new {model_name_snake}.
    \"\"\"
    {model_name_snake} = crud.{crud_module_name_import}.create(db=db, obj_in={model_name_snake}_in)
    return {model_name_snake}

@router.get("/", response_model=List[schemas.{schema_read_name}])
def read_{to_plural(model_name_snake)}(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    \"\"\"
    Retrieve {to_plural(model_name_snake)}.
    \"\"\"
    {to_plural(model_name_snake)} = crud.{crud_module_name_import}.get_multi(db, skip=skip, limit=limit)
    return {to_plural(model_name_snake)}

@router.get("/{{{pk_name_for_path}}}", response_model=schemas.{schema_read_name})
def read_{model_name_snake}(
    *,
    db: Session = Depends(deps.get_db),
    {pk_name_for_path}: {pk_type_hint}
) -> models.{model_name}:
    \"\"\"
    Get {model_name_snake} by {pk_name_for_path}.
    \"\"\"
    db_{model_name_snake} = crud.{crud_module_name_import}.get(db=db, id={pk_name_for_path})
    if not db_{model_name_snake}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{model_name} not found")
    return db_{model_name_snake}

@router.put("/{{{pk_name_for_path}}}", response_model=schemas.{schema_read_name})
def update_{model_name_snake}(
    *,
    db: Session = Depends(deps.get_db),
    {pk_name_for_path}: {pk_type_hint},
    {model_name_snake}_in: schemas.{schema_update_name}
) -> models.{model_name}:
    \"\"\"
    Update {model_name_snake}.
    \"\"\"
    db_{model_name_snake} = crud.{crud_module_name_import}.get(db=db, id={pk_name_for_path})
    if not db_{model_name_snake}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{model_name} not found")
    {model_name_snake} = crud.{crud_module_name_import}.update(db=db, db_obj=db_{model_name_snake}, obj_in={model_name_snake}_in)
    return {model_name_snake}

@router.delete("/{{{pk_name_for_path}}}", response_model=schemas.{schema_read_name})
def delete_{model_name_snake}(
    *,
    db: Session = Depends(deps.get_db),
    {pk_name_for_path}: {pk_type_hint}
) -> models.{model_name}:
    \"\"\"
    Delete a {model_name_snake}.
    \"\"\"
    db_{model_name_snake} = crud.{crud_module_name_import}.get(db=db, id={pk_name_for_path})
    if not db_{model_name_snake}:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{model_name} not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_{model_name_snake} = crud.{crud_module_name_import}.remove(db=db, id={pk_name_for_path})
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_{model_name_snake} is None and db_{model_name_snake} is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting {model_name}")
    return db_{model_name_snake} # Return the object that was found by get, as per response_model
"""

    router_file_path = ENDPOINTS_OUTPUT_DIR / f"{model_name_snake}.py"
    with open(router_file_path, "w") as f:
        f.write(router_content)
    print(f"  Generated FastAPI router file: {router_file_path}")

# Main generation function
def generate_all():
    print("Starting CRUD generation process...")
    # Ensure output directories exist
    SCHEMAS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CRUD_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENDPOINTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    models = get_sqlalchemy_models()
    if not models:
        print("No models found to process. Exiting.")
        return

    all_router_names_and_tags = []

    for model in models:
        model_name_singular = model.__name__
        model_name_snake = to_snake_case(model_name_singular)

        # Define schema names
        schema_base_name = f"{model_name_singular}Base"
        schema_create_name = f"{model_name_singular}Create"
        schema_update_name = f"{model_name_singular}Update"
        # Per Pydantic best practice, the main read schema is often just the model name
        schema_read_name = model_name_singular

        generate_pydantic_schemas(model, models)
        generate_crud_functions(model, schema_create_name, schema_update_name) # Updated call
        generate_fastapi_router(model, f"crud_{model_name_snake}", schema_read_name, schema_create_name, schema_update_name)

        all_router_names_and_tags.append({
            "module_name": model_name_snake,
            "router_variable_name": "router", # Assuming each endpoint file defines 'router'
            "tag_name": model_name_singular
        })

    # Update app/schemas/__init__.py
    schemas_init_content = "# This file makes Python treat the directory `schemas` as a package.\n\n"
    schemas_init_content += "# Import all Pydantic schemas for easier access\n"
    for model in models:
        model_name_singular = model.__name__
        model_name_snake = to_snake_case(model_name_singular)
        schema_base_name = f"{model_name_singular}Base"
        schema_create_name = f"{model_name_singular}Create"
        schema_update_name = f"{model_name_singular}Update"
        schema_read_name = model_name_singular # Main schema for read

        schemas_init_content += f"from .{model_name_snake} import {schema_base_name}, {schema_create_name}, {schema_update_name}, {schema_read_name}\n"

    schemas_init_content += "\n\n__all__ = [\n"
    for model in models:
        model_name_singular = model.__name__
        schemas_init_content += f"    \"{model_name_singular}Base\",\n"
        schemas_init_content += f"    \"{model_name_singular}Create\",\n"
        schemas_init_content += f"    \"{model_name_singular}Update\",\n"
        schemas_init_content += f"    \"{model_name_singular}\",\n" # Main read schema
    schemas_init_content += "]\n"

    with open(SCHEMAS_OUTPUT_DIR / "__init__.py", "w") as f:
        f.write(schemas_init_content)
    print(f"Updated {SCHEMAS_OUTPUT_DIR / '__init__.py'}")


    # Update app/crud/__init__.py
    crud_init_content = "# This file makes Python treat the directory `crud` as a package.\n\n"
    crud_init_content += "# Import all CRUD modules for easier access from services or routers\n"
    crud_items_to_export = []
    for model in models:
        model_name_singular = model.__name__
        model_name_snake = to_snake_case(model_name_singular)
        crud_module_name = f"crud_{model_name_snake}"
        # Option 1: Import specific functions (e.g., get, create, etc.)
        # crud_init_content += f"from .{crud_module_name} import get as get_{model_name_snake}, create as create_{model_name_snake} # ... etc\n"
        # crud_items_to_export.extend([f"get_{model_name_snake}", f"create_{model_name_snake}"])
        # Option 2: Import the module itself (simpler)
        crud_init_content += f"from . import {crud_module_name}\n"
        crud_items_to_export.append(crud_module_name)

    crud_init_content += "\n\n__all__ = [\n"
    for item_name in crud_items_to_export:
        crud_init_content += f"    \"{item_name}\",\n"
    crud_init_content += "]\n"

    with open(CRUD_OUTPUT_DIR / "__init__.py", "w") as f:
        f.write(crud_init_content)
    print(f"Updated {CRUD_OUTPUT_DIR / '__init__.py'}")


    # Update app/api/api_v1/api.py
    print(f"Updating main API router at {API_ROUTER_FILE}...")
    api_router_content = "from fastapi import APIRouter\n\n"
    api_router_content += "api_router = APIRouter()\n\n"
    for item in all_router_names_and_tags:
        api_router_content += f"from .{ENDPOINTS_OUTPUT_DIR.name} import {item['module_name']} as {item['module_name']}_router\n"
    api_router_content += "\n"
    for item in all_router_names_and_tags:
        api_router_content += f"api_router.include_router({item['module_name']}_router.{item['router_variable_name']}, prefix='/{to_plural(item['module_name'])}', tags=['{item['tag_name']}'])\n"

    API_ROUTER_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(API_ROUTER_FILE, "w") as f:
        f.write(api_router_content)

    # TODO: Modify app/main.py to include api_router (this might require more careful modification)
    print("CRUD generation process completed.")
    print("IMPORTANT: Review all generated files. This script provides a baseline and may need manual adjustments.")

if __name__ == "__main__":
    print("-----------------------------------------------------------------------------")
    print("WARNING: This script will overwrite existing files in app/schemas, app/crud, ")
    print("         and app/api/api_v1/endpoints without confirmation.")
    print("         Ensure you have version control or backups if necessary.")
    print("-----------------------------------------------------------------------------")
    # Add a small delay or a confirmation step in a real scenario
    # input("Press Enter to continue or Ctrl+C to abort...")
    generate_all()
