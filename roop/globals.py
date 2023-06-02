import onnxruntime

use_gpu = False
all_faces = False
log_level = 'quiet'
providers = onnxruntime.get_available_providers()

if 'TensorrtExecutionProvider' in providers:
    providers.remove('TensorrtExecutionProvider')
