from DeepfakeBench.training.detectors import DETECTOR
from DeepfakeBench.training.train import prepare_training_data, prepare_testing_data
import yaml
detector_path = '/mnt/data1/xuekang/workspace/DeepfakeBench/DeepfakeBench/training/config/config/detector/sbi.yaml'
with open(detector_path, 'r') as f:
        config = yaml.safe_load(f)
with open('/mnt/data1/xuekang/workspace/DeepfakeBench/DeepfakeBench/training/config/train_config.yaml', 'r') as f:
    config2 = yaml.safe_load(f)

if 'label_dict' in config:
    config2['label_dict']=config['label_dict']
config.update(config2)
config['dataset_json_folder'] = '/mnt/data1/xuekang/workspace/DeepfakeBench/DeepfakeBench/preprocessing/dataset_json'
config['ddp'] = False

model_class = DETECTOR[config['model_name']]
model = model_class(config)
train_data_loader = prepare_training_data(config)
# prepare the testing data loader
test_data_loaders = prepare_testing_data(config)
import pdb
pdb.set_trace()
data_dict = next(iter(train_data_loader))
predictions = model(data_dict)
losses = model.get_losses(data_dict, predictions)