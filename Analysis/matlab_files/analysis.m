clear all; clc;
%load('/home/aransena/thesis_ws/Analysis/matlab_files/watch_participants.mat')
load('/home/aransena/thesis_ws/Analysis/matlab_files/robot_participants.mat')
gender = transpose(gender);
age = transpose(age);
% disp('age')
% age(1,1)
% disp('game')
% game(1,:)
% disp('gender')
% gender(1,1)
% disp('spatial')
% spatial(1,1)
%size(age(:,1))

%anovan(xbox_man(:,1),{gender(:,1),age(:,1),game(:,2)},'model','interaction','varnames',{'gender','age','game'})
%anovan(xbox_sa(:,1),{gender(:,1),age(:,1)},'model','interaction','varnames',{'gender','age'})
%anovan(watch_man(:,1),{gender(:,1),age(:,1)},'model','interaction','varnames',{'gender','age'})
%anovan(watch_sa(:,1),{gender(:,1),age(:,1)},'model','interaction','varnames',{'gender','age'})
kurtosis(xbox_man(:,1))
kurtosis(xbox_sa(:,1))
kurtosis(watch_man(:,1))
kurtosis(watch_sa(:,4))
disp('----------')
skewness(xbox_man(:,1))
skewness(xbox_sa(:,1))
skewness(watch_man(:,1))
skewness(watch_sa(:,4))
disp('----------')
%C = categorical(age(:,1),[1 2 3 4],{'18-24','25-34','35-44','45+'})
histogram(age(:,1))
disp('----------')

x = [xbox_man(:,1),xbox_sa(:,1),watch_man(:,1),watch_sa(:,4)];
z = [double(age(:,1))];
rho = partialcorr(x,z)

t = table(age(:,1),xbox_man(:,1),xbox_sa(:,1),watch_man(:,1),watch_sa(:,4),...
'VariableNames',{'age','x_m','x_sa','w_m','w_sa'});
Meas = table([1 2 3 4]','VariableNames',{'Measurements'});
rm = fitrm(t,'x_m-w_sa~age','WithinDesign',Meas);
out = manova(rm,'By','age')
[d,p,stats] = manova1(x,game(:,2))
manovacluster(stats)

t = table(gender(:,1),xbox_man(:,1),xbox_sa(:,1),watch_man(:,1),watch_sa(:,4),...
'VariableNames',{'gender','x_m','x_sa','w_m','w_sa'});
Meas = table([1 2 3 4]','VariableNames',{'Measurements'});
rm = fitrm(t,'x_m-w_sa~gender','WithinDesign',Meas);
out = manova(rm,'By','gender');

t = table(game(:,2),xbox_man(:,1),xbox_sa(:,1),watch_man(:,1),watch_sa(:,4),...
'VariableNames',{'game','x_m','x_sa','w_m','w_sa'});
Meas = table([1 2 3 4]','VariableNames',{'Measurements'});
rm = fitrm(t,'x_m-w_sa~game','WithinDesign',Meas);
out = manova(rm,'By','game');
%manova(rm)

%[manovatbl,A,C,D] = manova(rm)
%A{1}
%A{2}