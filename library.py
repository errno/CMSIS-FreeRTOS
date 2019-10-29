# PlatformIO library build script (in combination with library.json)
# Author: Frank Leon Rose
# Copyright (c) 2019

# Example platformio.ini
#   [env:cmsis-atmel]
#   platform = atmelsam
#   board = adafruit_feather_m0
#   framework = cmsis
#   build_flags =
#     -D FREERTOS_HEAP_IMPLEMENTATION=heap_1.c
#     -D FREERTOS_MCU_FAMILY=ARM_CM0
#   lib_deps = https://github.com/frankleonrose/CMSIS-FreeRTOS

# In addition, it is necessary to place FreeRTOSConfig.h and RTE_Components.h
# files in the project source directory.

# See https://github.com/frankleonrose/FreeRTOS_M0 sample project.

from os.path import isdir, join, realpath

Import('env')

build_flags = env.ParseFlags(env['BUILD_FLAGS'])
defines = {k: v for (k, v) in build_flags.get("CPPDEFINES")}

mcu_family = defines.get("FREERTOS_MCU_FAMILY")
heap_implementation = defines.get("FREERTOS_HEAP_IMPLEMENTATION", "heap_1.c")

global_env = DefaultEnvironment()
platform = global_env.PioPlatform()
CMSIS_FRAMEWORK = platform.get_package_dir("framework-cmsis")

env.Append(
    CPPPATH=[
        realpath(join("Source", "portable", "GCC", mcu_family)),
        realpath(join(CMSIS_FRAMEWORK, "CMSIS", "RTOS2", "Include")),
        join(env.get("PROJECTSRC_DIR")), # For FreeRTOSConfig.h
    ]
)

env.Append(
    SRC_FILTER=[
        "-<*>",
        "+<CMSIS/RTOS2/FreeRTOS/Source/*.c>",
        "+<Source/*.c>",
        "+<Source/portable/*.c>",
        "+<Source/portable/GCC/%s/*.c>" % mcu_family,
        "+<Source/portable/MemMang/%s>" % heap_implementation,
    ]
)
