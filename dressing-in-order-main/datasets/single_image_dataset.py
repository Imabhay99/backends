import os
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Dataset

class SingleImageDataset(Dataset):
    def __init__(self, image_path, opt):
        self.image_dir = image_path
        self.image_list = [
            os.path.join(self.image_dir, f)
            for f in os.listdir(self.image_dir)
            if f.lower().endswith((".jpg", ".png", ".jpeg"))
        ]
        self.transform = transforms.Compose([
            transforms.Resize((opt.load_size, opt.crop_size)),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, index):
        path = self.image_list[index]
        image = Image.open(path).convert("RGB")
        return {
            "image": self.transform(image),
            "path": path
        }
