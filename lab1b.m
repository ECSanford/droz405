function [d, t] = lab1b(np,nd,nw)
if (nargin < 1), np=1e7; nd=4; nw=4; end
np = 1e7, nw = 8;
hp = gcp('nocreate');
if isempty(hp), hp=parpool(nw); end
A = randn(np, nd); B = randn(np, nd);
d = zeros(np,1);
tic;
parfor i = 1:np
    for j = 1:nd
        d(i) = (B(i,1)-A(i,1)).^2 + (B(i,2)-A(i,2)).^2;
    end
    d(i) = sqrt(d(i));
end
t = toc;
disp(t);
%delete(hp);