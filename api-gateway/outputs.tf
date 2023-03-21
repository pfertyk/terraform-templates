output "api_url" {
  description = "Public URL of this API"
  value = "${aws_apigatewayv2_stage.stage.invoke_url}${aws_lambda_function.lambda.function_name}"
}
