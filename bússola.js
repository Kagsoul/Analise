```ts
export const Router = new class RouteManager {
  private default_target = document.body;
  private routes: Map<string, Routing> = new Map;

  define_target(target: HTMLElement) {
    this.default_target = target;
  }

  define_route(route: string, f: RouteFn) {
    if (f.name == "") throw new Error("Anonymous functions are not allowed as routes");
    if (route == "/") return this.routes.set("/", {
      route: f,
      subroutes: new Map
    });
    const split = route.split("/");
    const last = split.pop()!;
    let current = this.routes;
    for (const path of split) {
      current.set(path, {
        subroutes: current = new Map,
      });
    }
    current.set(last, {
      subroutes: new Map,
      route: f
    });
  }

  goto(dst: string) {
    if (dst == ".") {
      dst = location.pathname;
    }
    history.replaceState({}, "", "/");
    this.moveto(dst);
  }
  //This function manages the routing but it's unstable so it's better to make it private
  private moveto(dst: string) {
    history.pushState({}, "", dst);
    const pathname = location.pathname.split("/");
    pathname.shift();
    let lastpath = pathname.pop();
    if (dst == "..") lastpath = pathname.pop();
    let current = this.routes;
    const params = [];
    for (const path of pathname) {
      if (current.has(path)) current = current.get(path)?.subroutes;
      else if (current.has("dynroute")) {
        current = current.get("dynroute")?.subroutes;
        params.push(path);
      } else return this.goto("404");
    }
    const last = current.get(lastpath!) ?? (current.has("dynroute") && params.push(lastpath!), current.get("dynroute"));
    if (!last?.route) {
      this.goto("404");
      return;
    }
    const component = last.route(params, new Map);
    if (component instanceof Promise) component.then(el => el.parent(this.default_target));
    else component.parent(this.default_target);
  }
};
```