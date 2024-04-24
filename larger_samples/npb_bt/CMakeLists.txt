cmake_minimum_required(VERSION 3.11)
project(perf_prog_npb_bt)

set_property(GLOBAL PROPERTY C_STANDARD 11)

if(MSVC)
  add_compile_options(/W4)
else()
  add_compile_options(-Wall -Wextra -Wno-unknown-pragmas -Wno-unused-parameter)
endif()

file(GLOB_RECURSE SOURCE_FILES CONFIGURE_DEPENDS src/*.c src/*.h)

link_libraries(m)

set(SIZES w s a b c)
set(OPTIMIZATION_LEVELS 0 1 2 3 s fast)
set(OPT_FLAGS gcse-after-reload ipa-cp-clone loop-interchange loop-unroll-and-jam peel-loops predictive-commoning split-loops split-paths tree-loop-distribution tree-partial-pre unswitch-loops) 

foreach(OPT_LEVEL ${OPTIMIZATION_LEVELS})
  foreach(SIZE ${SIZES})
    set(P npb_bt_${SIZE}_O${OPT_LEVEL})
    add_executable(${P} ${SOURCE_FILES})
    target_include_directories(${P} PRIVATE src/w)
    target_compile_options(${P} PRIVATE -O${OPT_LEVEL})
  endforeach()
endforeach()

foreach(OPT_FLAG ${OPT_FLAGS})
  # string(REGEX REPLACE "[-=]" "_" OPT_NAME ${OPT_FLAG})
  foreach(SIZE ${SIZES})
        set(P npb_bt_${SIZE}${OPT_NAME})
    add_executable(${P} ${SOURCE_FILES})
    target_include_directories(${P} PRIVATE src/w)
    target_compile_options(${P} PRIVATE -O2 -f${OPT_FLAG})
  endforeach()
endforeach()
