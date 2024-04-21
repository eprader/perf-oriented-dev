cmake_minimum_required(VERSION 3.11)
project(perf_prog_npb_bt)

set_property(GLOBAL PROPERTY C_STANDARD 11)

file(GLOB_RECURSE SOURCE_FILES CONFIGURE_DEPENDS src/*.c src/*.h src/sprng2.0/*.c src/sprng2.0/*.h)
include_directories(src/sprng2.0/include)

link_libraries(m)
add_definitions(-DLittleEndian, -DAdd__)

set(OPTIMIZATION_LEVELS 0 1 2 3)

foreach(OPT_LEVEL ${OPTIMIZATION_LEVELS})
  set(P ssca2_O${OPT_LEVEL})

  add_executable(${P} ${SOURCE_FILES})
  target_compile_options(${P} PRIVATE -O${OPT_LEVEL})
endforeach()
