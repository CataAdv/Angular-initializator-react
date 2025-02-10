
import os


def loader(file):
    with open(file, 'r') as f:
        return f.read()


def Component_Creator( base_path="." ) :

    path                    =           input("enter component location: ") or base_path
    component_name          =           input("enter component name: ")
    component_group         =           input("enter component group-family: ")
    folder_path             =           os.path.join(path, component_name)

    try:
        os.makedirs(folder_path, exist_ok=True)

        print(f"Component created {folder_path}")


        css                 =           input("You want a .css file? (Y/N): ").strip().lower()


        file_content = {   

            f"{component_name}.{component_group}.types.ts" : loader("Components/TypescriptTypes/index.md")          
                .replace("ComponentTypescript",             f"{component_name}_{component_group}_types"),                         


            f"{component_name}.{component_group}.component.tsx" : loader("Components/ContentPage/index.md")            
                .replace("ComponentReact",                  f"{component_name.capitalize()}{component_group.capitalize()}Component")     
                .replace("ComponentTypescriptUrl",          f"{component_name}.{component_group}.types")                                      
                .replace("ComponentTypescript",             f"{component_name}_{component_group}_types"),


            f"{component_name}.{component_group}.routes.tsx" : loader("Components/TypescriptRoutes/index.md")   
                .replace("ComponentTypescriptRoutes",       f"{component_name}_{component_group}_routes")                     
                .replace("ComponentReactUrl",               f"{component_name}.{component_group}.component")                                       
                .replace("ComponentTypescriptRoute",        f"{component_name}")                                               
                .replace("ComponentReact",                  f"{component_name.capitalize()}{component_group.capitalize()}Component"),            


            f"{component_name}.{component_group}.tsx" :     loader("Components/index/index.md")               
                .replace("ComponentTypescriptRoutesUrl",    f"{component_name}.{component_group}.routes")                  
                .replace("ComponentTypescriptRoutes",       f"{component_name.capitalize()}{component_group.capitalize()}Routes")         
                .replace("ComponentReactUrl",               f"{component_name}.{component_group}.component")                          
                .replace("ComponentReact",                  f"{component_name.capitalize()}{component_group.capitalize()}Component")  
                .replace("Component",                       f"{component_name.capitalize()}{component_group.capitalize()}"),
        
        }


        if css == 'y' :
            file_content[f"{component_name}.{component_group}.style.css"] = loader("Components/css/index.md").replace("ComponentCss", f"{component_name}_{component_group}_style")


        for file, content in file_content.items() : 

            file_path = os.path.join(folder_path, file)


            with open(file_path, 'w') as f :
                f.write(content)
    

    except Exception as file_errors :
        print(f"error at creating {file_errors}")



Component_Creator();