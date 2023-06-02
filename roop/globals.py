import onnxruntime

use_gpu = False
all_faces = False
debug = False
providers = onnxruntime.get_available_providers()

if 'TensorrtExecutionProvider' in providers:
    providers.remove('TensorrtExecutionProvider')
