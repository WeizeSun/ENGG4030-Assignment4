function [n] = q3b()
    R = dlmread('rsq3b');
    R = R(:, 2);
    m = length(R);
    n = betam(m) * m^2 / sum(2.^(-R));
end

function [betam_output] = betam(m)
    fun = @(u) (log2((2+u)./(1+u)).^m);
    betam_output = (m*integral(fun, 0, Inf))^-1;
end