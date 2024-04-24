cmake_minimum_required(VERSION 3.10)
project(perf_oriented_prog_samples)

set_property(GLOBAL PROPERTY C_STANDARD 11)

if(MSVC)
  add_compile_options(/W4 /WX)
else()
  add_compile_options(-Wall -Wextra -Wpedantic -Werror)
endif()

set(OPTIMIZATION_LEVELS 0 1 2 3 s fast)
set(OPT_FLAGS gcse-after-reload ipa-cp-clone loop-interchange loop-unroll-and-jam peel-loops predictive-commoning split-loops split-paths tree-loop-distribution tree-partial-pre unswitch-loops version-loops-for-strides)

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
  # string(REGEX REPLACE "[-=]" "_" OPT_NAME ${OPT})

  add_executable(mmul_${OPT} mmul/mmul.c)
  target_compile_options(mmul_${OPT} PRIVATE -O2 -f${OPT})

  add_executable(delannoy_${OPT} delannoy/delannoy.c)
  target_compile_options(delannoy_${OPT} PRIVATE -O2 -f${OPT})

  add_executable(nbody_${OPT} nbody/nbody.c)
  target_link_libraries(nbody_${OPT} m)
  target_compile_options(nbody_${OPT} PRIVATE -O2 -f${OPT})

  add_executable(qap_${OPT} qap/qap.c)
  target_compile_options(qap_${OPT} PRIVATE -O2 -f${OPT})

  add_executable(filesearch_${OPT} filesearch/filesearch.c)
  target_compile_options(filesearch_${OPT} PRIVATE -O2 -f${OPT})

  add_executable(filegen_${OPT} filegen/filegen.c)
  target_compile_options(filegen_${OPT} PRIVATE -O2 -f${OPT})
endforeach()
