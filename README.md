# Pocket export list

This task export Pocket list to files grouped by tag.

It requieres an access token. You can get it using fxneumann's [OneClickPocket](http://reader.fxneumann.de/plugins/oneclickpocket/auth.php).

## Arguments

| Parameter        | Type   | Description                | Required | Default value |
|------------------|--------|----------------------------|----------|---------------|
| --help (or   -h) |        | Show help message and exit | False    |               |
| --consumerkey    | String | Pocket consumer key.       | True     |               |
| --accesstoken    | String | Pocket access token.       | True     |               |
| --outputfolder   | String | Output folder.             | True     |               |

## Example

### Call

>py main.py --consumerkey 91...4a --accesstoken 1c...5c --outputfolder c:/tmp

## References

- [Pocket API: Retrieving a User's Pocket Data](https://getpocket.com/developer/docs/v3/retrieve)
- [Python Requests post() Method](https://www.w3schools.com/python/ref_requests_post.asp)
- [Python requests.Response Object](https://www.w3schools.com/python/ref_requests_response.asp)