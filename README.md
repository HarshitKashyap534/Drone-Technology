# References
Midas Repo: 
https://github.com/isl-org/MiDaS/tree/master

Midas with Torch Reference: 
https://pytorch.org/hub/intelisl_midas_v2/

# Setup 
- Windows 10 
- Python 3.10.9
- VS Code 1.84.0 

# Special Notes
1. DO NOT NAME YOUR FILE `midas.py`, WILL GET ERRORS! 
2. I renamed path to `isl-org/MiDaS` in the load command 
3. Need to install timm, which has torch image models 
```bash
pip install timm
```
4. Pip install torch with cuda 
```bash 
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```