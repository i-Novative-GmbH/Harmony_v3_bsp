# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

def instantiateComponent(bspComponent):
    # LED_RED: PB17
    Database.setSymbolValue("core", "PIN_204_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_204_FUNCTION_NAME", "LED_RED")
    Database.setSymbolValue("core", "PIN_204_DIR", "Out")
    Database.setSymbolValue("core", "PIN_204_LAT", "Low")

    # LED_GREEN: PB15
    Database.setSymbolValue("core", "PIN_205_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_205_FUNCTION_NAME", "LED_GREEN")
    Database.setSymbolValue("core", "PIN_205_DIR", "Out")
    Database.setSymbolValue("core", "PIN_205_LAT", "Low")

    # LED_BLUE: PA21
    Database.setSymbolValue("core", "PIN_327_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_327_FUNCTION_NAME", "LED_BLUE")
    Database.setSymbolValue("core", "PIN_327_DIR", "Out")
    Database.setSymbolValue("core", "PIN_327_LAT", "Low")

    #SWITCH USER_BUTTON: PC10
    Database.setSymbolValue("core", "PIN_146_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_146_FUNCTION_NAME", "USER_BUTTON")
    Database.setSymbolValue("core", "PIN_146_PU", "True")
    Database.setSymbolValue("core", "PIN_146_DIR", "")

    BSP_NAME = "sam_a7d65_curiosity"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"},
        {"attrib":"int", "symbol":"BSP_CUSTOM_PIO_INTERRUPT", "label":"PIO Interrupt"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT"}]


    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
