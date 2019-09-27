function [d, t] = lab1d(np,nd,nl)
if (nargin < 1), np=1e7; nd=2; nl=8; end
hp = gcp('nocreate');

np = 1e7; nd = 8;
spmd
    A = randn(np, nd); B = randn(np, nd);
    d = zeros(np/nl,1);
    tic;
    for i = 1:np/nl
        for j = 1:nd
            d(i) = d(i) + (B(i,j)-A(i,j)).^2;
        end
        d(i) = sqrt(d(i));
    end
    t = toc;
    disp(t);
    
end
delete(hp);