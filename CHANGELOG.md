## v0.5.3

* Introduce `options` parameter for `client.notify` and `workflows.trigger` methods
    * This parameter can be used to pass in additional options to the request
    * Pass in an `idempotency_key` value via options to prevent duplicate notifications from being sent to your service
