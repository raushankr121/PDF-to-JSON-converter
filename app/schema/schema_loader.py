import json
import os


class SchemaLoader:

    @staticmethod
    def load(schema_path: str) -> dict:
        """
        Loads a JSON schema file from the given path.
        If the path is not found directly, falls back to checking inside `app/schema/`.
        """
        if not os.path.exists(schema_path):
            filename = os.path.basename(schema_path)
            alt_path = os.path.join("app", "schema", filename)
            if os.path.exists(alt_path):
                schema_path = alt_path
            else:
                default_path = os.path.join("app", "schema", "jee.json")
                if os.path.exists(default_path):
                    schema_path = default_path
                else:
                    raise FileNotFoundError(f"Schema file not found: {schema_path}")

        with open(schema_path, "r", encoding="utf-8") as f:
            return json.load(f)
