from mrjob.job import MRJob

class MRAmigosPorIdade(MRJob):

    def mapper(self, _, line):
        (ID, nome, idade, numAmigos) = line.split(',')
        
        yield nome.lower(), 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRAmigosPorIdade.run()