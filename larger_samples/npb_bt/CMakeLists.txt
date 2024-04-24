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
set(OPT_FLAGS -fgcse-after-reload -fipa-cp-clone -floop-interchange -floop-unroll-and-jam -fpeel-loops -fpredictive-commoning -fsplit-loops -fsplit-paths -ftree-loop-distribution -ftree-partial-pre -funroll-completely-grow-size -funswitch-loops -fversion-loops-for-strides ) 

foreach(OPT_LEVEL ${OPTIMIZATION_LEVELS})
  foreach(SIZE ${SIZES})
    set(P npb_bt_${SIZE}_O${OPT_LEVEL})
    add_executable(${P} ${SOURCE_FILES})
    target_include_directories(${P} PRIVATE src/w)
    target_compile_options(${P} PRIVATE -O${OPT_LEVEL})
  endforeach()
endforeach()

foreach(OPT_FLAG ${OPT_FLAGS})
  foreach(SIZE ${SIZES})
    set(P npb_bt_${SIZE}_${OPT_FLAG})
    add_executable(${P} ${SOURCE_FILES})
    target_include_directories(${P} PRIVATE src/w)
    target_compile_options(${P} PRIVATE -O2 ${OPT_FLAG})
  endforeach()
endforeach()
