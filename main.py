from fastapi import FastAPI, HTTPEException
from pydantic import BaseModel

app = FastAPI(title= "Tasks CRUD API: gabriel")


class TaskCreat(BaseModel):
    title: str
    description: str = ""
    done: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None


class Task(TaskCreat):
    id: int


    task: dict[int,Task]= {}
    next_id=1


    @app.get("/")
    del health_check():
        return{"massage":"API de tasks online"}


    @app.get("/tasks", response_model= list[Task])
    def list_tasks():
        return list(tasks.values())


    @app.post("/tasks", response_model=Task, status_code=201)
    def create_task(payload: TaskCreat):
        global next_id

        task = Task(id=next_id, **payload.model_dump())
        tasks[next_id] = task
        next_id += 1
        return task


    @app.get("/tasks/{task_id}", response_model = Task)
    def get_task(task_id: int):
        task = tasks.get(task_id)
        if not task:
            raise HTTPEException(status_code=404, detail="Task não encontrada")
       return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    task = tasks.get(task_id)
    if not task:
        raise HTTPEException(status_code=404, detail=Task não encontrada)

data = task.model_dump()
updates = payload.model_dump(exclude_unset=True)
data.update(updates)

update_task = Task(**data)
tasks(task_id) = update_task
return update_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: id):
    if task_id not in tasks:
        raise HTTPEException(status_code=204, detail="Task não encontrada")

    del tasks[task_id]    