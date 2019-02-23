# libdxvk-rpm
RPM packaging for Linux native DXVK library.  
Patches are from this pull request: https://github.com/doitsujin/dxvk/pull/926

## Build
```shell
yum install meson ninja-build wine-devel glslang vulkan-devel
./create-package.sh
```
