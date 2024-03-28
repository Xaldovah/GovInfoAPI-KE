# GovInfoAPI-KE Documentation

Welcome to the GovInfoAPI-KE documentation! This document provides detailed information about the API service, including its endpoints, functionality, and usage.

## Overview

GovInfoAPI-KE is an API service designed to provide users with information about political representatives in Kenya, including Members of Parliament, Senators, Governors, Members of County Assembly (MCAs).

## Endpoints

The API provides the following endpoints for accessing representative data:

1. **GET /mps**: Retrieve information about Members of Parliament.
2. **GET /senators**: Retrieve information about Senators.
3. **GET /governors**: Retrieve information about Governors.
4. **GET /mcas**: Retrieve information about Members of County Assembly (MCAs).

## Authentication and Authorization

This is an open source API to know your representative hence you are not required to authenticate to access any information.

## Usage

To use the GovInfoAPI-KE service, send HTTP GET requests to the appropriate endpoints listed above.

For more details about each endpoint and its parameters, please refer to the API documentation.

## Examples

Here are some examples of how to use the GovInfoAPI-KE service:

1. Retrieve information about all Members of Parliament:
- GET /mps/

2. Retrieve information about a Member of a specific constituenct:
- GET /mps/kamkunji/

3. Retrieve information about all Senators:
- GET /senators/

4. Retrieve information about Senators representing a specific county:
- GET /senators/nairobi/

5. Retrieve information about all Governors:
- GET /governors/

6. Retrieve information about Governors representing a specific county:
- GET /governors/mombasa county/

7. Retrieve information about all Governors:
- GET /mcas/

8. Retrieve information about an MCA representing a specific ward:
- GET /mcas/ward/

## Feedback and Support

If you have any questions, feedback, or need assistance with using GovInfoAPI-KE, please don't hesitate to reach out to me. I am here to help!
