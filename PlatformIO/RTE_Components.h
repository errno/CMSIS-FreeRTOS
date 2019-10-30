#ifndef RTE_COMPONENTS_H
#define RTE_COMPONENTS_H

// Configuration required by CMSIS RTOS components.

/*
 * Define the Device Header File:
 */
#if !defined(CMSIS_device_header)
#error Please define the CMSIS_device_header in your build flags. Should be something like "sam.h" or "stm32f4xx.h" (including quotes in the macro value).
#endif

// The following are selectively defined by Keil but not used in source.
// #define RTE_RTOS_FreeRTOS_CONFIG_RTOS2
// #define RTE_RTOS_FreeRTOS_CONFIG
// #define RTE_RTOS_FreeRTOS_CORE
// #define RTE_RTOS_FreeRTOS_TIMERS
// #define RTE_Compiler_EventRecorder
// #define RTE_Compiler_EventRecorder_DAP

// Define one of the following if using heap implementations 1 or 5 and CMSIS RTOS 1 or 2 functions.
// They control release of task memory on thread completion.
#if FREERTOS_HEAP_IMPLEMENTATION == 1
#define RTE_RTOS_FreeRTOS_HEAP_1        /* RTOS FreeRTOS Heap 1 */
#elif FREERTOS_HEAP_IMPLEMENTATION == 5
#define RTE_RTOS_FreeRTOS_HEAP_5        /* RTOS FreeRTOS Heap 5 */
#endif

#endif /* RTE_COMPONENTS_H */
