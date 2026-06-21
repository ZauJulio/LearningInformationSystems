import { Command } from "../../interfaces/command";
import { Editor } from "../Editor";

export class EditorUndoRedoCommand implements Command {
  constructor(private readonly editor: Editor) {}
  
  execute(): void {
    this.editor.undo();
  }

  undo(): void {
    this.editor.redo();
  }
}
