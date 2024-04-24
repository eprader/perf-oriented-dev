cmake_minimum_required(VERSION 3.10)
project(perf_oriented_prog_samples)

set_property(GLOBAL PROPERTY C_STANDARD 11)

if(MSVC)
  add_compile_options(/W4 /WX)
else()
  add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

set(OPTIMIZATION_LEVELS 0 1 2 3 s fast)
set(OPT_FLAGS -fgcse-after-reload -fipa-cp-clone -floop-interchange -floop-unroll-and-jam -fpeel-loops -fpredictive-commoning -fsplit-loops -fsplit-paths -ftree-loop-distribution -ftree-partial-pre -funswitch-loops -fversion-loops-for-strides) 

# Loop over optimization levels and create a separate target for each
foreach(OPT ${OPTIMIZATION_LEVELS})
  add_executable(mmul_O${OPT} mmul/mmul.c)
  target_compile_options(mmul_O${OPT} PRIVATE -O${OPT})

  add_executable(delannoy_O${OPT} delannoy/delannoy.c)
  target_compile_options(delannoy_O${OPT} PRIVATE -O${OPT})

  add_executable(nbody_O${OPT} nbody/nbody.c)
  target_compile_definitions(nbody_O${OPT} PRIVATE -DM=400)
  target_link_libraries(nbody_O${OPT} m)
  target_compile_options(nbody_O${OPT} PRIVATE -O${OPT})

  add_executable(qap_O${OPT} qap/qap.c)
  target_compile_options(qap_O${OPT} PRIVATE -O${OPT})

  add_executable(filesearch_O${OPT} filesearch/filesearch.c)
  target_compile_options(filesearch_O${OPT} PRIVATE -O${OPT})

  add_executable(filegen_O${OPT} filegen/filegen.c)
  target_compile_options(filegen_O${OPT} PRIVATE -O${OPT})
endforeach()

foreach(OPT ${OPT_FLAGS})
  string(REGEX REPLACE "[-=]" "_" OPT_NAME ${OPT})

  add_executable(mmul${OPT_NAME} mmul/mmul.c)
  target_compile_options(mmul${OPT_NAME} PRIVATE -O2 ${OPT})

  add_executable(delannoy${OPT_NAME} delannoy/delannoy.c)
  target_compile_options(delannoy${OPT_NAME} PRIVATE -O2 ${OPT})

  add_executable(nbody${OPT_NAME} nbody/nbody.c)
  target_link_libraries(nbody${OPT_NAME} m)
  target_compile_options(nbody${OPT_NAME} PRIVATE -O2 ${OPT})

  add_executable(qap${OPT_NAME} qap/qap.c)
  target_compile_options(qap${OPT_NAME} PRIVATE -O2 ${OPT})

  add_executable(filesearch${OPT_NAME} filesearch/filesearch.c)
  target_compile_options(filesearch${OPT_NAME} PRIVATE -O2 ${OPT})

  add_executable(filegen${OPT_NAME} filegen/filegen.c)
  target_compile_options(filegen${OPT_NAME} PRIVATE -O2 ${OPT})
endforeach()
