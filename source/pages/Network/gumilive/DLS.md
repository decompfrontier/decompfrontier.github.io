# DLS
This is the latest version of the Gumi API server found inside Brave Frontier, this server
manages the dynamic background and game api url information.

The game checks if this server is HTTPS and the CA certificate matches the one of the game
server.

**URL**: https://api-sl.gl.gumi.sg

## Request: /dls
**Type**: GET

The DLS request accepts and returns a JSON object called "SREE".

Request and response format:
```
{
	"SREE": "content"
}
```

The content of SREE is encrypted with AES-CBC and the content is then encoded with Base64.

AES key: `7410958164354871`

AES IV: `Bfw4encrypedPass`

The content of a decrypted SREE as follows:

```
{
	(todo...)
}
```

| Name | Description | Optional | Possible values |
| ---- | ----------- | -------- | ------ |
| game | Game name | no | string |
| resource | CDN server where resources will be downloaded | no | string |
| mstv | Game version | no | number |
| gumilive | Login server | no | string |
| bgimage | Background image to show during login | no | string |
| force | Forces the game to show a message and then exit | yes | true/false |
| force_msg | Message to show to force close the game | yes | string |
