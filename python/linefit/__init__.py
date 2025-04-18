'''
# @date: 2025-04-18 18:29
# @author: Qingwen Zhang  (https://kin-zhang.github.io/)
# Copyright (C) 2025-now, RPL, KTH Royal Institute of Technology
# 
# This file is part of HiMo (https://kin-zhang.github.io/HiMo).
# If you find this repo helpful, please cite the respective publication as 
# listed on the above website.
'''

__version__ = "1.1.0"

import numpy as np
import linefit_bind

class ground_seg:
    def __init__(self, config_path=None):
        """
        config_path (str): path to the config file, if None, use default parameters
        """
        if config_path is None:
            self.linefit_fn = linefit_bind.ground_seg()
        else:
            self.linefit_fn = linefit_bind.ground_seg(config_path)
    
    def run(self, points):
        """
        Parameters
        ----------
        points (np.ndarray): point cloud data, shape (N, 3), 3 for x, y, z
        """
        points = np.ascontiguousarray(points.astype(np.float32))
        labels = np.array(self.linefit_fn.run(points[:, :3])).astype(np.uint8)
        return labels