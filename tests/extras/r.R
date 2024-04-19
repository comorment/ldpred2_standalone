# test script checking that all installed/required libraries are present

# Load the testthat package
library(testthat)

# List of libraries to check
libraries_to_check <- c(
    "argparser",
    "bigreadr",
    "bigsnpr",
    "devtools",
    "data.table",
    "dplyr",
    "essentials",
    "eulerr",
    "ggplot2",
    "grDevices",
    "IRkernel",
    "methods",
    "optparse",
    "R.utils",
    "RColorBrewer",
    "stringr",
    "tidyverse",
    "tools"
    )

# Define a test
test_that("Required libraries are installed", {
  missing_libraries <- setdiff(libraries_to_check, installed.packages()[, "Package"])
  expect_true(length(missing_libraries) == 0, 
              sprintf("Missing libraries: %s", paste(missing_libraries, collapse = ", ")))
})