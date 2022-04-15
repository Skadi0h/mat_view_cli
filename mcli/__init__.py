import json
import fire
from mcli.engine.inspect import ViewInspector
from pyfiglet import Figlet


def create_view(config):
    with open(config, "r") as file:
        settings = json.load(file)
        args_values = settings['config']['value']

    db_url = f"postgresql+psycopg2://{args_values['db_user']}:{args_values['db_password']}" \
             f"@{args_values['db_host']}:{args_values['db_port']}/{args_values['db_name']}"
    ViewInspector(db_url=db_url,
                  db_name=args_values['db_name'],
                  sql_module=args_values['sql_module'],
                  sql_full_path=args_values['sql_full_path']
                  ).register_view(args_values['view_name'],
                                  sql_name=args_values['sql_name'],
                                  create_index=args_values['create_index'],
                                  index_name=args_values['index_name'],
                                  index_col_name=args_values['index_column'],
                                  render_model=args_values['render_model'],
                                  url=args_values['url'],
                                  api_class_name_snake_case=args_values['api_class_name_snake_case'],
                                  api_class_name_pascal_case=args_values['api_class_name_pascal_case'],
                                  root_name=args_values['root_folder'],
                                  schema_name=args_values['db_schema'])


if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('MCLI!'))
    fire.Fire(create_view)
