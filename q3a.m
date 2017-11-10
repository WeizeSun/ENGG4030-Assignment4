function [n] = q3a()
    R = dlmread('rsq3a');
    R = R(:, 2);
    m = length(R);
    alpha = (gamma(-1/m) * (1 - 2 ^(1/m)) / log(2)) ^ (-m);
    n = alpha * m * 2 ^ (sum(R) / m);
end