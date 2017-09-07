
aws apigateway create-rest-api --name 'customer-retention-probability' --description 'Return the probability of a custer leaving the health fund' --profile personal
# Create Resource /customer-retention
aws apigateway create-resource --name 'customer-retention'