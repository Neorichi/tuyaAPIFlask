# TuyaAPIFlask

Using the TuyaSmart url request to create a API with Flask and Python3 to turn on/off you own switch


## Steps

1. Buy [WiFi TECKIN 16A 3300W](https://www.amazon.es/Inteligente-TECKIN-Temporizador-Aplicaciones-Cualquier/dp/B07SK1CVVV/ref=sr_1_16?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=teckin&qid=1605567893&sr=8-16)
2. Download Tuya Smart APP in your mobile
3. Pair device with your mobile APP
4. Change with your credentials

```python
data={
      "userName": "xxxxxx@gmail.com", # change with your email Tuya Smart APP
      "password": "xxxxxxxxxx", # change with your password Tuya Smart APP
      "countryCode": "1",
      "bizType": "tuya",
      "from": "tuya",
}
```
5. Get you ID device
5.1 Edit you device
5.2 Device information
5.3 Copy ID Virtual and paste into switchId value

```python
switchId = "xxxxxxxxxxx"
```

## Usage

<pre> pip3 install -r requirements.txt </pre>

To switch on/off
<pre> python3 main.py </pre>


License
----

MIT
