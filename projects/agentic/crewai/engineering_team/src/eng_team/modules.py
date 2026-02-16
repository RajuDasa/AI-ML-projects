from pydantic import BaseModel, Field

class ModuleSchema(BaseModel):
    '''
    Design details for single self-contained module.
    '''
    module_name:str = Field(description="Python code file name")
    class_name:str = Field(description="python class name in this module")
    purpose:str = Field(description="Detailed description for this module. Includes class and methods signature and their purpose")

class ModuleList(BaseModel):
    '''collection of modules, complementing a big design'''
    modules: list[ModuleSchema] = Field(description="collection of ModuleSchema objects, complementing complete code design")