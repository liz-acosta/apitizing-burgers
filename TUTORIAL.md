
# The Importance of SDKs in the Developer Experience

*Skip to the [Tutorial](#tutorial).*

What do Developer Experience and playing cards have in common? At first glance, the two seem pretty disparate, but for Idan Gazit, senior director of research at GitHub, playing cards are a lesson in the journeys developers undertake when attempting to execute on a task. “Building software is like having a giant house of cards in our brains,” [says Gazit](https://github.blog/2023-06-08-developer-experience-what-is-it-and-why-should-you-care/), “Tiny distractions can knock it over in an instant. DevEx is ultimately about how we contend with that house of cards.”

Not many modern developers can get away without having to make an API call to some sort of external service. While APIs are a powerful developer tool, software development kits – or “SDKs” – help enable seamless integration and as such, are integral to a sophisticated Developer Experience. With so many products and solutions available to developers, an SDK can make or break a customer.

In this tutorial, we will show you how to use FastAPI, OpenAPI, and Speakeasy to create the SDK your developers deserve.

## What is FastAPI?

Based on the open standards for APIs set forth by OpenAPI and JSON Schema, [FastAPI](https://fastapi.tiangolo.com/) is a web framework for building RESTful APIs in Python. Unlike Flask and Django, FastAPI is optimized for developing high-performance APIs with minimal code that takes advantage of standard type hints. Because FastAPI is based on OpenAPI (formerly known as the Swagger Specification), using the framework means baked-in compatibility with other development tools as well as automatic API documentation creation.

Another powerful benefit of building with the OpenAPI standards is the ability to create SDKs and client libraries from a FastAPI application.

## What is OpenAPI?

The [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) (OAS) “defines a standard, programming language-agnostic interface description for HTTP APIs, which allows both humans and computers to discover and understand the capabilities of a service without requiring access to source code, additional documentation, or inspection of network traffic.” In other words, OAS both abstracts away and standardizes how different components of software can interact with each other according to RESTful architecture. The result is a single source of truth for an API that can be used for testing, automation, and creating both code and documentation.

While writing to a specification may seem like a constraint, OpenAPI’s standardization enables more flexibility and a more programmatic approach to API development.

## What is Speakeasy?

[Speakeasy](https://www.speakeasyapi.dev/product/sdks) is on a mission to accelerate innovation by making it radically simple to create and consume APIs. Ever since Stripe launched their transactions API product, APIs have become the defacto method by which B2B companies expose their core functionality. However, even the best APIs can’t overcome a poor developer experience. Speakeasy integrates with some of the most popular API frameworks to deliver production-ready SDKs that empower developers and take APIs to the next level.

Follow along to learn how to create an SDK with FastAPI and Speakeasy.

# Tutorial

In this tutorial, you will use a FastAPI application to generate an OpenAPI spec and then use Speakeasy to create a Python SDK from that spec. 

## Prerequisites

1. Python 3.8+
2. A [Speakeasy account](https://www.speakeasyapi.dev/)

## Setup

1. Clone the code from the Speakeasy apitizing-burgers repo # TODO: link for this
2. Change directory into the project directory
3. Check out the `tutorial` branch
4. In the project root directory, create a virtual environment: `virtualenv venv`
5. Activate the virtual environment: `source venv/bin/activate`
6. Install FastAPI: `pip install "fastapi[all]"`
7. Install Speakeasy using Homebrew: `brew install speakeasy-api/homebrew-tap/speakeasy`

Now you have everything you need to complete the tutorial.

## A Quick Tour of the Code

This tutorial uses a project built with the FastAPI framework called “apitizing-burgers” that handles burgers and orders. In the project root directory is a directory called `app` where you can find a file called `main.py`. This file is where the application lives.

You will also see a file called `save_openapi.py`. This file is not part of the application and contains helper code for saving and transforming the OpenAPI spec created by FastAPI.

Throughout this tutorial, you will modify the code on the `tutorial` branch of the repo. This code is commented out and indicated with a `TODO` comment for your searching convenience. The `main` branch of this repo contains a finished version of this tutorial.

## Spinning Up the FastAPI Server

1. From the `app` directory, run the following: `​​uvicorn main:app --reload`
2. Navigate to `http://127.0.0.1:8000/docs` where you should see a user interface documenting the apitizing-burgers APIs

## Taking a Look at the OpenAPI Spec

FastAPI gives you an OpenAPI spec out of the box. At `http://127.0.0.1:8000/docs` you should see the linked text `/openapi.json`. Clicking on this link will show you the OpenAPI spec created by FastAPI in (unformatted) JSON.

For a more human readable version of the OpenAPI spec, from the project root directory, run `python app/save_openapi.py`. This will save the specification as a .json file.

## Creating an SDK From the OpenAPI Spec

### Add Servers

In order to use Speakeasy to create an SDK from the OpenAPI spec, you need to add servers to the specification since FastAPI doesn’t require this.

1. In `main.py`, locate the line where a FastAPI object is created and uncomment the `servers` argument
2. In `main.py`, locate the `custom_openapi` method that creates the variable `openapi_schema` and uncomment the `servers` argument from the `get_openapi` function
3. From the project root directory, run `python app/save_openapi.py`

### Validate the OpenAPI Spec

The Speakeasy CLI comes with additional tooling and support to help you create the SDKs your API deserves.

1. Run `speakeasy` from the project root directory to see a list of available commands
2. Use your arrow keys to navigate to `validate` and press Return to see another list of available commands
3. Use your arrow keys to navigate to `openapi` and press Return
4. Now you can provide the filepath to the OpenAPI spec, which in this case should be `./openapi.json`

This will initialize the Speakeasy OpenAPI validatior. If your spec is valid, you should see the following:

```
You can upload your schema to Speakeasy using the following command:

speakeasy api register-schema --schema=./openapi.json

```
(To learn more about registering your schema with the Speakeasy API, refer to the documentation [here](https://www.speakeasyapi.dev/docs/speakeasy-cli/api/register-schema).)

### Generate the Client SDK

With the validity of your OpenAPI spec confirmed, you can create an SDK.

1. You can either navigate through the Speakeasy CLI menus to select `generate` and follow the prompts or you can run `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk`

Here’s how to interpret that command:

* `speakeasy generate` is the Speakeasy CLI subcommand that initializes the Speakeasy client SDK generation
* `sdk` is a Speakeasy CLI argument that indicates you want to generate a client SDK from the OpenAPI spec
* The `--schema` flag indicates where the OpenAPI spec to use is located
* The `--lang` flag indicates which language you want to create an SDK for
* The `--out` flag indicates where you want your SDK to be saved

So in the command `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk` you are telling Speakeasy that you would like to generate a Python SDK from the schema found at `./openapi.json` and save it to `./sdk`.

To learn more about the Speakeasy CLI, please refer to the [documentation](https://www.speakeasyapi.dev/docs/speakeasy-cli/README).

If the generation was successful, you will find a new `sdk` directory with the docs and code for your new Python SDK.

## Enhancing and Customizing Your SDK

Congratulations on creating your first SDK with Speakeasy! With the hardest parts of SDK creation handled by Speakeasy, you are free to focus on enhancing the developer experience.

### Add More Information to Your SDK

You can leverage the FastAPI class to add more information to your SDK.

1. In `main.py`, locate the line where a FastAPI object is created and uncomment the `summary` and `description` arguments
2. In `main.py`, locate the `custom_openapi` method that creates the variable `openapi_schema` and uncomment the `summary` and `description` arguments from the `get_openapi` function

### Customize Your SDK Method Names

If you look inside your new Python SDK in `/src/sdk/sdk.py`, you will notice methods with redundant names such as `​​create_burger_burger_post`. This is because when generating the OpenAPI spec, FastAPI uses a default naming pattern to ensure unique operation IDs. While these IDs are indeed unique, they do not result in the most user-friendly method names. Fortunately, you can customize how these IDs are generated.

The best way to do this is taking advantage of FastAPI’s `generate_unique_id_function` parameter.

1. In `main.py`, locate the line where a FastAPI object is created and uncomment the `generate_unique_id_function` argument

### Recreate Your SDK

Now let's see how these changes are reflected in your SDK.

1. From the project root directory, run `python app/save_openapi.py` to overwrite the `openapi.json` file
2. Run the Speakeasy SDK generation command again: `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk`

Now check the method names in the SDK. The redundancy should be gone, replaced by method names that are a lot more user-friendly. Additionally, the SDK now contains a summary and description. 

## Further Enhancing Your SDK for Both Machines and Humans

### Group Operations Together

You can use `tags` to group operations together to reflect the separation of duties in your code in your OpenAPI spec and in your SDK.

In `main.py`, search for the commented-out `tags` and uncomment them. Each route will have one. With these tags, your OpenAPI spec and your SDK will now be grouped into operations that involve burgers and operations that involve orders:

1. Generate a new spec by running `python app/save_openapi.py`
2. Re-run `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk` to create a new SDK

You should notice that now you have a file called `burger.py` that contains the operations related to burgers and a file called `order.py` that contains the operations related to orders.

### Add Metadata to Your Tags

You can take this one step further by adding metadata to your tags.

1. In `main.py`, uncomment the `openapi_tags` parameter passed into the FastAPI class
2. Generate a new spec by running `python app/save_openapi.py`
3. Re-run `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk` to create a new SDK

Now the `Burger` and `Order` SDK classes should contain more information.

## Speakeasy OpenAPI Extensions

So far, these customizations leverage the OpenAPI functionality within FastAPI, but Speakeasy enables you to add even more to your SDK via OpenAPI extensions.

### Add Retries Globally and Per Route

1. To add retries globally, in `main.py`, locate the `custom_openapi` method that creates the variable `openapi_schema` and uncomment the block of code that adds the `x-speakeasy-retries` key and value to the `openapi_schema` object
2. To add retries to the `get` route, in `main.py`, locate the route that gets a burger and uncomment the `openapi_extra` argument

### Override Method Names

You can use the `x-speakeasy-name-override` extension to match on and override naming patterns.

In this example, you will override all instances of “read” in the SDK method names to “fetch” using Speakeasy.

1. To add a name override globally, in `main.py`, locate the `custom_openapi` method that creates the variable `openapi_schema` and uncomment the block of code that adds the `x-speakeasy-name-override` key and value to the `openapi_schema` object

By adding this, you are telling Speakeasy to use a regular expression to replace operation IDs that match the expression to the value specified for `methodNameOverride` – which, in this case, is “fetch.”

To see your changes in your SDK:

1. Generate a new spec by running `python app/save_openapi.py`
2. Re-run `speakeasy generate sdk --schema ./openapi.json --lang python --out ./sdk` to create a new SDK

You should now see retries in your SDK as well as the method name override.

Speakeasy supports a suite of SDK customizations. To learn more about how to customize your SDK, please refer to the documentation [here](https://www.speakeasyapi.dev/docs/customize-sdks).

To learn more about integrating Speakeasy with FastAPI, please refer to the documentation [here](https://www.speakeasyapi.dev/docs/api-frameworks/fastapi).

## But That’s Just the Beginning …

Speakeasy can not only create your SDKs, we can manage them too. With a Speakeasy managed SDK, you can focus your engineering resources on product development. Speakeasy helps you deliver value to your customers quickly by providing the SDKs that enable developers to seamlessly integrate your product.  

All you need is an OpenAPI spec. Let Speakeasy do the rest.

To learn more about Speakeasy, check out our documentation [here](https://www.speakeasyapi.dev/docs). To speak with someone on the team, get in touch with us [here](https://www.speakeasyapi.dev/contact).