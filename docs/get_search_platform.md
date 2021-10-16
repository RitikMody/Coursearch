## Retrieve MOOCs by search term and platform

`GET` /api?{searchTerm}/{site}

### Parameters:

| Name  | Type | In | Description |
| ------------- | ------------- | ------------- | ------------- |
| searchTerm*  | string | path | Indicates the topic / MOOC name to search the API for across all platforms. Good examples for this parameter would be deep learning, graphic design, writing. |
| site*  | string | path | Indicates the platform to mine MOOC data from. Can take any of the following values: `coursera`, `udemy `, `pluralsight` or `udacity` |