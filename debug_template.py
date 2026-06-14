import os, sys, importlib.util  
p='C:\\Users\\user\\Documents\\LEGACY_DIGITAL_FOREVER_PROTOTYP\\LEGACY_DIGITAL_FOREVER_PROTOTYP\\app.py'  
sys.path.insert(0, os.path.dirname(p))  
spec=importlib.util.spec_from_file_location('legacy_app', p)  
m=importlib.util.module_from_spec(spec)  
spec.loader.exec_module(m)  
print('loader', type(m.app.jinja_loader), getattr(m.app.jinja_loader, 'searchpath', None))  
print('template_folder', m.app.template_folder) 
