linefit
---

[![Stable Version](https://img.shields.io/pypi/v/linefit?label=stable)](https://pypi.org/project/linefit/#history)
[![Python Versions](https://img.shields.io/pypi/pyversions/linefit)](https://pypi.org/project/linefit/)
[![Download Stats](https://img.shields.io/pypi/dm/linefit)](https://pypistats.org/packages/linefit)

linefit is a ground segmentation algorithm for 3D point clouds. 
This repo we setup a python binding for the original C++ code and push to pypi for easy installation through `pip install linefit`.

Author: C++ code from [Lorenz Wellhausen](https://github.com/lorenwel), python package from [Qingwen Zhang](https://kin-zhang.github.io/).

Running on macOS, Windows and Linux, with Python Version >= 3.8.

Available in: <a href="https://github.com/Kin-Zhang/linefit"><img src="https://img.shields.io/badge/Windows-0078D6?st&logo=windows&logoColor=white" /> <a href="https://github.com/Kin-Zhang/linefit"><img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black" />  <a href="https://github.com/Kin-Zhang/linefit"><img src="https://img.shields.io/badge/mac%20os-000000?&logo=apple&logoColor=white" /> </a>

<!--  -->
📜 Change Log:
- 2025-04-18: Add `__init__.py` to the package with `ascontiguousarray` to avoid unexpected point error reading, add package to the latest python (3.13) also. Rename the default branch to `main`.
- 2024-07-03: Speed up nanobind `np.array` <-> `std::vector<Eigen:: Vector3d>` conversion and also `NOMINSIZE` in make. Speed difference: 0.1s -> 0.01s. Based on [discussion here](https://github.com/wjakob/nanobind/discussions/426).
- 2024-02-15: Initial version.

## 0. Setup

Choose one of the following options to install the package (recommended to use Option A `pip install linefit`):

Option A: Install from pypi `pip install linefit`

Option B: Clone this repo and run following to build:
```bash
pip install git+https://github.com/Kin-Zhang/linefit
python3 -c 'import linefit; print("linefit ground seg lib import success")'
```

Dependencies for demo:
```bash
# for reading data and visualization
pip install numpy open3d
```

## 1. Run the example

Demo usage:
```python
pc_data = np.load("kitti_pc0.npy") # [N, 3]
groundseg = ground_seg("config.toml")
label = np.array(groundseg.run(pc_data[:,:3])) # [N, 1]
# 1: ground, 0: non-ground for this pc_data
```

You can check the full example script in [example.py](example.py). If you run the example script, it will directly show a default effect of demo data.

```bash
python example.py
```

A window will pop up and show the ground segmentation result.
![](./assets/docs/demo.png)

## Parameter description

Parameters are set in `assets/config.toml`. I also provided several popular datasets' parameters in [assets/config](assets/config). Note that the origin pose should in sensor link but base link of the robot or vehicle. The process step can be found in [DeFlow](https://github.com/KTH-RPL/DeFlow/blob/main/dataprocess/README.md)/[SeFlow](https://github.com/KTH-RPL/SeFlow/blob/main/dataprocess/README.md).

TL;DR: tune the `sensor_height` to offset the ground point z to `0`. Others are optional for better performance. If you are interested in the details, please read the following.


This algorithm works on the assumption that you known the height of the sensor above ground. 
Therefore, **you have to adjust the `sensor_height`** to your robot specifications, otherwise, it will not work.

The default parameters should work on the KITTI dataset.

### Ground Condition
- **sensor_height**  Sensor height above ground.
- **max_dist_to_line**  maximum vertical distance of point to line to be considered ground.
- **max_slope**  Maximum slope of a line.
- **min_slope**  Minimum slope of a line.
- **max_fit_error**  Maximum error a point is allowed to have in a line fit.
- **max_start_height**  Maximum height difference between new point and estimated ground height to start a new line.
- **long_threshold**  Distance after which the max_height condition is applied.
- **max_height**  Maximum height difference between line points when they are farther apart than *long_threshold*.
- **line_search_angle**  How far to search in angular direction to find a line. A higher angle helps fill "holes" in the ground segmentation.

### Segmentation

- **r_min**  Distance at which segmentation starts.
- **r_max**  Distance at which segmentation ends.
- **n_bins**  Number of radial bins.
- **n_segments**  Number of angular segments.

### Other

- **n_threads**  Number of threads to use.

## Acknowledgement & Citation

The original C++ code is from [the repo we forked: lorenwel/linefit_ground_segmentation](https://github.com/lorenwel/linefit_ground_segmentation).

The original methods are described in the following paper:
```
@inproceedings{himmelsbach2010fast,
  title={Fast segmentation of 3d point clouds for ground vehicles},
  author={Himmelsbach, Michael and Hundelshausen, Felix V and Wuensche, H-J},
  booktitle={Intelligent Vehicles Symposium (IV), 2010 IEEE},
  pages={560--565},
  year={2010},
  organization={IEEE}
}
```

This Python package is developed during HiMo project, please consider to cite our paper if this python package is helpful for your research:

```
@article{zhang2025himo,
    title={HiMo: High-Speed Objects Motion Compensation in Point Cloud},
    author={Zhang, Qingwen and Khoche, Ajinkya and Yang, Yi and Ling, Li and Sina, Sharif Mansouri and Andersson, Olov and Jensfelt, Patric},
    year={2025},
    journal={arXiv preprint arXiv:2503.00803},
}
```

More python binding examples can be found in our other project:
- [dufomap](https://github.com/KTH-RPL/dufomap): a dynamic awareness mapping framework. Remove dynamic points in a raw map.
- [dztimer](https://github.com/KTH-RPL/dztimer): a breakout timer for python code.


<!-- 
This function is a part of our new paper, which is under review. If you use this python function, please try to cite our paper to support us:
```
TODO
``` -->
