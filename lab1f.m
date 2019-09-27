function [t] = lab1f(np, nd, nl)
if (nargin < 1), np = 1e7; nd = 2; nl = 4; end
hp = gcp('nocreate');

if isempty(hp), hp = parpool(nl); end

dA = distributed.randn(np, nd);
dB = distributed.randn(np, nd);

tic;
dc = sqrt(sum((dA-dB).^2,2));
C = gather(dc);
t = toc;
disp(t);

delete(hp);