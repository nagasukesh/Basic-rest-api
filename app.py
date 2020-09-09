from flask import Flask,jsonify,request

api=Flask(__name__)

tasks = [
    {
        'id' : 1,
        'name' : 'flask',
        'done' : 'True',
    },
    {
        'id' : 2,
        'name' : 'Fast API',
        'Done' : 'True',
    }
]

@api.route('/tasks')
def index() :
    return jsonify(tasks)

@api.route('/tasks',methods=['PUT'])
def add_task() :
    task={'id' : 3,'name' : 'testing', 'done' : 'False' }
    tasks.append(task)
    return jsonify(tasks)

@api.route('/tasks/<int:tid>', methods=['POST'])
def update_task(tid) :
    for task in tasks :
        if task['id'] == tid :
            task['name'] += ' updated'
    return jsonify(tasks)

@api.route("/tasks/<int:tid>",methods=['DELETE'])
def delete_task(tid) :
    for task in tasks :
        if task['id'] == tid :
            tasks.remove(task)
    return jsonify(tasks)



@api.errorhandler(404)
def bar(error):
        return "ERROR 404"

@api.errorhandler(405)
def bar(error):
        return "THE METHOS IS NOT ALLOWED"




if __name__ == '__main__':
    api.run(debug=True)


