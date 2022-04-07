Create database GashaImpactDB;

use GashaImpactDB;

create table Conta(
	id int Not Null auto_increment primary key,
    login varchar(15) not null,
    senha varchar(20) not null
);

create table Personagem(
	id int not null auto_increment primary key,
    nome varchar(25) not null,
    tipo varchar(15) not null,
    estrela int not null
);

create table PersonagensDaConta(
	personagemid int not null,
    contaid int not null,
    refinopersonagem int not null
);

alter table PersonagensDaConta
 add foreign key (personagemid) references personagem (id);

alter table PersonagensDaConta
 add foreign key (contaid) references Conta(id);
 
alter table PersonagensDaConta
drop foreign key personagensdaconta_ibfk_1;
 
 insert into personagem (nome, tipo, estrela)
 values ('Diluc', 'Pyro', 5);
 
 select * from personagem;
 
 15:14:24	DROP TABLE `gashaimpactdb`.`personagem`	Error Code: 3730. Cannot drop table 'personagem' referenced by a foreign key constraint 'personagensdaconta_ibfk_1' on table 'personagensdaconta'.	0.109 sec
