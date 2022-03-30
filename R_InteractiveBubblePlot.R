library(plotly)

data <- read.csv("/Users/matt.held/Library/CloudStorage/OneDrive-EdgewoodCollege/Classes/Senior Year/Spring 2022/Introduction to Data Analytics - CS 305/Week 11/solar.csv")

data$State <- as.factor(c('California','Arizona','Nevada','New Mexico','Colorado','Texas','North Carolina','New York'))

fig <- plot_ly(data, x = ~Number_of_Solar_Plants, y = ~Generation_GWh, text = ~State, type = 'scatter', mode = 'markers', size = ~Efficiency, color = ~State, colors = 'Paired',
               marker = list(opacity = 0.5, sizemode = 'diameter'))
fig <- fig %>% layout(title = 'Solar Panel Efficiency with Quantity and Generation',
                      xaxis = list(showgrid = FALSE),
                      yaxis = list(showgrid = FALSE),
                      showlegend = FALSE)

fig
