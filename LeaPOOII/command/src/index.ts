import * as readline from "readline";

import { EditorUndoRedoCommand } from "./Editor/Commands/EditorUndoRedoCommand";
import { Editor } from "./Editor/Editor";

class Main {
  private rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  private inputStd = "";
  private editor: Editor = new Editor("sigaa");
  private editorUR: EditorUndoRedoCommand = new EditorUndoRedoCommand(
    this.editor
  );

  public async write() {
    console.clear();

    do {
      this.insert(String(await this.getInput()));

      switch (this.inputStd.toLowerCase()) {
        case "exit":
          return;
        case "clear":
          console.clear();
          break;
        case "undo":
          this.undo();
          break;
        case "redo":
          this.redo();
          break;
        case "output":
          this.output();
          break;
        default:
          this.editor.write(this.inputStd);
          this.output();
          break;
      }
    } while (this.inputStd !== "exit");
  }

  private getInput = () =>
    new Promise((resolver) =>
      this.rl.question("Input: ", (res) => resolver(res))
    );

  private insert = (text: string) => {
    this.inputStd = text;
  };

  public undo = () => {
    this.editorUR.execute();
    this.output();
  };

  public redo = () => {
    this.editorUR.undo();
    this.output();
  };

  private output = () => {
    console.log("Output: ", this.editor.text);
  };

  public getText = () => this.editor.text;
}

const main = new Main();
main.write();
