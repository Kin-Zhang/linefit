nanobind_add_module(linefit_bind MODULE NOMINSIZE linefit_ext.cpp)
target_link_libraries(linefit_bind PRIVATE gm_lib)
install(TARGETS linefit_bind LIBRARY DESTINATION .)