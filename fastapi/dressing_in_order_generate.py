import os
import sys

# Add path to import from dressing-in-order-main
sys.path.append(os.path.abspath("../dressing-in-order-main"))

from options.test_options import TestOptions
from generate_all import generate_all

def generate_tryon(person_path, cloth_path, output_path):
    # Simulate argparse options
    opt = TestOptions().parse(save=False)
    
    opt.dataroot = "../dressing-in-order-main"
    opt.results_dir = os.path.dirname(output_path)
    opt.name = "DIORv1_64"
    opt.input_person = person_path
    opt.input_cloth = cloth_path
    opt.phase = "test"
    opt.checkpoints_dir = "./checkpoints"
    opt.save_output = True

    # Run model
    generate_all(opt)
