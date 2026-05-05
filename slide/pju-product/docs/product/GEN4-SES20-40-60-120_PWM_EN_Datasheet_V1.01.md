---
source_file: GEN4-SES20-40-60-120_PWM_EN_Datasheet_V1.01.pdf
extracted_at: 2026-05-05T23:05:06.347956Z
pages_extracted: 4
---


## Page 1

SR-SES Series
Human motion sensing wireless dimming type LED solar
street light controller
SES120/60/40/20 （-WB/IR）Gen4
• Very low sleep current for long-distance transportation and storage.
• High accuracy and high efficiency PWM charge with constant voltage.
• 10-period programmable load power/time control.
• Human motion infrared/microwave sensing function, with sensing delay time settable.
• Lithium battery charge and discharge high and low temperature protection, with operating temperature
settable.
• A variety of lithium battery intelligent power modes, with load power adjustable automatically according
SES20 SES40 SES60 SES120
to the battery level.
• High precision digital step-up constant current control algorithm, ensuring high efficiency and high
010 101
101 010 on on
010 101
constant current accuracy. PWM
• Infrared wireless communication, allowing for setting/reading parameters, reading status, etc.
Power
• Multiple protections such as battery/PV reverse polarity protection, LED short-circuit/open-circuit/limited 100%
IP68
Features 10%
100% 30% soc
power protection, etc.
www.szshuori.com

### Table 1 (Page 1)

|  |
|  |


### Table 2 (Page 1)

| on on |
|  |


### Table 3 (Page 1)

| Power |
| 100% 10% 100% 30% soc |


### Table 4 (Page 1)

|  |
|  |


### Table 5 (Page 1)

|  |
|  |


### Table 6 (Page 1)

|  |
|  |


### Table 7 (Page 1)

|  |
| IP68 |


### Table 8 (Page 1)

| www.szshuori.com |  |


## Page 2

Exterior
Mounting hole Switch wire
Waterproof wire Connecting wire
Temperature sensor
Temperature sensor
Motion sensor
Connecting wire Connecting wire
Wiring D i a g ram
Gen4 Intelligent PWM
Solar Charge Controller
With Step-up LED Driver
COM
www.szshuori.com

### Table 1 (Page 2)

| Exterior Mounting hole Switch wire Waterproof wire Connecting wire Temperature sensor Temperature sensor Motion sensor Connecting wire Connecting wire Wiring D i a g ram Gen4 Intelligent PWM Solar Charge Controller With Step-up LED Driver COM |
| www.szshuori.com |


## Page 3

1、SES40 has two indicators, red and blue.
2、SES20/SES60/SES120 has one indicator, red.
75
www.szshuori.com
85 34
Φ3.5
25
95
104
53
4X 3,2
100
85.5
75
Φ3.5
State Indicators
Controller system
Color Status Description
status
Steady on Load is turned on Discharging
Single flash Battery works properly, in standby mode Idle
Blue Slow flash In charging Charging
Double flash Lithium battery is fully charged Fully charged
Quick flash Lithium battery bms overcharge protection E-BMS
Controller system
Color Status Description
status
Load is open circuited Open circuit
Load is short circuited Short circuit
Slow flash PV overvoltage PV panel overvoltage
Red BAT overvoltage Battery overvoltage
Over temperature Over temperature
Single flash
(One flash per Overdischarge, sleep /
10 seconds)
Controller system
Color Status Description
status
Steady on System is normal Idle/discharging
Slow flash In charging Charging
Short circuit/open circuit/over discharge/
Red Quick flash System failure PV panel overvoltage/battery overvoltage
/EBMS/over temperature
Single flash
(One flash per Overdischarge, sleep /
10 seconds)
Installation D i m ensions
Model: SES40
Model: SES20
Overall dimensions: 72*72*26mm
Overall dimensions: 104*52*20mm
Mounting dimensions: 58*54mm
Mounting dimensions: 95*35mm
Mounting hole diameter: φ4.0
Mounting hole diameter: φ3.2
Model: SES60 Model: SES120
Overall dimensions: 82*57.5*20mm Overall dimensions: 82*100*20mm
Mounting dimensions: 43*75mm Mounting dimensions: 86*75mm
Mounting hole diameter: φ3.5 Mounting hole diameter: φ3.5

### Table 1 (Page 3)

| Color | Status | Description | Controller system status |
| Blue | Steady on Single flash Slow flash Double flash Quick flash | Load is turned on | Discharging |
|  |  | Battery works properly, in standby mode | Idle |
|  |  | In charging | Charging |
|  |  | Lithium battery is fully charged | Fully charged |
|  |  | Lithium battery bms overcharge protection | E-BMS |
| Color | Status | Description | Controller system status |
| Red | Slow flash Single flash (One flash per 10 seconds) | Load is open circuited | Open circuit |
|  |  | Load is short circuited | Short circuit |
|  |  | PV overvoltage | PV panel overvoltage |
|  |  | BAT overvoltage | Battery overvoltage |
|  |  | Over temperature | Over temperature |
|  |  | Overdischarge, sleep | / |


### Table 2 (Page 3)

| Color | Status | Description | Controller system status |
| Red | Steady on | System is normal | Idle/discharging |
|  | Slow flash | In charging | Charging |
|  | Quick flash | System failure | Short circuit/open circuit/over discharge/ PV panel overvoltage/battery overvoltage /EBMS/over temperature |
|  | Single flash (One flash per 10 seconds) | Overdischarge, sleep | / |


### Table 3 (Page 3)

| 53 | 4X 3,2 |


### Table 4 (Page 3)

|  | 85.5 |
|  |  |
| 75 | Φ3.5 |


## Page 4

Parameters
Items Values Adjustable Default
Model SES20 SES40 SES60 SES120
Remote control type Microwave sensing: -WB；Infrared sensing: - IR
Controller and sensor are Controller and sensor are
Combined mode
integrated split
System voltage 12V 12V/24V
Zero load loss < 10mA/12V <10mA/12V；<15mA/24V
Sleep loss < 0.8mA/12V <0.8mA/12V；<8mA/24V
Load current 50mA～1000mA 50mA～2000mA 50mA～4000mA √ 330mA
Load voltage 15V～45V 15V～60V
40W/12V 60W/12V
Maximum load power 20W/12V 40W/12V
60W/24V 120W/24V
Load conversion
90% ～ 96%
efficiency
Load current accuracy < 3%
Maximum charge current 5A 10A 20A √ Medium
Solar input voltage ≤ 25V ≤ 55V
Over voltage Charge voltage + 2V
Charge voltage 9.00V ～17.00V, settable √ 12.45V
Charge return voltage 9.00V ～17.00V, settable √ 12.00V
Over discharge voltage 9.00V ～17.00V, settable √ 9.20V
Over discharge return
9.00V ～17.00V, settable √ 10.20V
voltage
Light control voltage 3V ～ 11V √ 5V
Light control delay 5s～60s/2min～60min √ 10S
Operating temperature -35℃ ～ +65℃
IP rating IP67
Weight 120g 150g 170g 300g
www.szshuori.com

### Table 1 (Page 4)

| Items | Values |  |  |  | Adjustable | Default |
| Model | SES20 | SES40 | SES60 | SES120 |  |  |
| Remote control type | Microwave sensing: -WB；Infrared sensing: - IR |  |  |  |  |  |
| Combined mode | Controller and sensor are integrated |  | Controller and sensor are split |  |  |  |
| System voltage | 12V |  | 12V/24V |  |  |  |
| Zero load loss | < 10mA/12V |  | <10mA/12V；<15mA/24V |  |  |  |
| Sleep loss | < 0.8mA/12V |  | <0.8mA/12V；<8mA/24V |  |  |  |
| Load current | 50mA～1000mA | 50mA～2000mA |  | 50mA～4000mA | √ | 330mA |
| Load voltage | 15V～45V |  | 15V～60V |  |  |  |
| Maximum load power | 20W/12V | 40W/12V | 40W/12V 60W/24V | 60W/12V 120W/24V |  |  |
| Load conversion efficiency | 90% ～ 96% |  |  |  |  |  |
| Load current accuracy | < 3% |  |  |  |  |  |
| Maximum charge current | 5A | 10A |  | 20A | √ | Medium |
| Solar input voltage | ≤ 25V |  | ≤ 55V |  |  |  |
| Over voltage | Charge voltage + 2V |  |  |  |  |  |
| Charge voltage | 9.00V ～17.00V, settable |  |  |  | √ | 12.45V |
| Charge return voltage | 9.00V ～17.00V, settable |  |  |  | √ | 12.00V |
| Over discharge voltage | 9.00V ～17.00V, settable |  |  |  | √ | 9.20V |
| Over discharge return voltage | 9.00V ～17.00V, settable |  |  |  | √ | 10.20V |
| Light control voltage | 3V ～ 11V |  |  |  | √ | 5V |
| Light control delay | 5s～60s/2min～60min |  |  |  | √ | 10S |
| Operating temperature | -35℃ ～ +65℃ |  |  |  |  |  |
| IP rating | IP67 |  |  |  |  |  |
| Weight | 120g | 150g | 170g | 300g |  |  |
