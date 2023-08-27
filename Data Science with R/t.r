library(glmnet)
library(Matrix)

# 데이터 생성
set.seed(123)
X <- matrix(rnorm(100*5), 100, 5)
y <- X %*% c(1, 2, 3, 4, 5) + rnorm(100) * 0.1

# 릿지 회귀 (Ridge Regression)
ridge_model <- glmnet(X, y, family = "gaussian", alpha = 0)
ridge_predictions <- predict(ridge_model, newx = X)
ridge_mse <- mean((y - ridge_predictions)^2)

# 라쏘 회귀 (Lasso Regression)
lasso_model <- glmnet(X, y, family = "gaussian", alpha = 1)
lasso_predictions <- predict(lasso_model, newx = X)
lasso_mse <- mean((y - lasso_predictions)^2)