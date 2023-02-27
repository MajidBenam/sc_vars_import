% unrolled by hand from qing_milexpense.xlsx
data = textread('expense.csv','','delimiter','\t'); % warfare expenses
miny = min(data(:,1));
maxy = max(data(:,2));
expend = zeros(maxy -  miny + 1,1);
offy = miny - 1;
for i = 1:12
  sy = data(i,1); ey = data(i,2); ex = data(i,3);
  % NOTE that expenses in 1721 overlap with expenses from 1715-1726; are these double counted?
  mexp = ex/(ey - sy + 1); 
  for y = sy:ey
    expend(y - offy) = expend(y - offy) + mexp;
  end
end
figure
plot(miny:maxy,expend);
xlabel('Year'); ylabel('Warfare expenses (M silver taels)')
grid on
fid = fopen('expenses_per_year.csv','w');
fprintf(fid,'Year,Expenditure\n');
for i = 1:length(expend)
  fprintf(fid,'%d,%.1f\n',offy+i,expend(i));
end
fclose(fid);

