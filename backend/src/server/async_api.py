from flask import Blueprint, jsonify
from flask import request
from kombu.exceptions import OperationalError


class CountdownAsyncAPI(Blueprint):
    def __init__(self, name, import_name, celery, *args):
        self._celery_task = celery
        self._config = None
        super(CountdownAsyncAPI, self).__init__(name, import_name, *args)

        @self.route('/numbers_async', methods=['GET'])
        
            return request.host

        # Polling of celery tasks
        @self.route('/progress/<task_id>', methods=['GET'])
        def progress(task_id):
            job = self._celery_task.AsyncResult(task_id)
            result = job.result
            if job.state == 'PENDING':
                ret = {
                    'status': job.state,
                    'msg': {},
                    'code': 404
                }
            elif job.state != 'FAILURE':
                ret = {
                    'status': job.state,
                    'msg': {
                        'solution': result.get('solution'),
                        'recursions': result.get('recursions'),
                        'exec_time': result.get('exec_time')
                    },
                    'code': 200
                }

            else:
                ret = {
                    'status': job.state,
                    'msg': {
                        'code': result[0],
                        'message': result[1]
                    },
                    'code': 400
                }

            code = ret.pop('code')
            return jsonify(ret), code

    def register(self, app, options, first_registration=False):
        super(CountdownAsyncAPI, self).register(app, options, first_registration)
        self._config = app.config
