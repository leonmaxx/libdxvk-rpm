# libdxvk-rpm
RPM packaging for Linux native DXVK library.  
Patches are from this pull request: https://github.com/doitsujin/dxvk/pull/926

## Build
```shell
yum install meson ninja-build wine-devel glslang vulkan-devel
./create-package.sh
```
## Copr Repository
Pre-built packages ready for testing is in this copr repository: https://copr.fedorainfracloud.org/coprs/leonmaxx/wine-dxvk/
